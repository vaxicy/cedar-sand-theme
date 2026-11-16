
// Cedar & Sand Theme — deep cedar green and warm sand gold
import { readFile } from 'node:fs/promises';

const CEDAR_SAND = {
  forest: '#1E3B2F',
  deepCedar: '#16291F',
  litCedar: '#3D5C49',
  sage: '#79836C',
  sand: '#B29D6B',
  paleSand: '#D9CBAE',
  bone: '#F1EFE2',
};

export class CedarGrove {
  constructor(grove = 'North ridge') {
    this.grove = grove;
    this.palette = CEDAR_SAND;
    this.trees = Object.keys(CEDAR_SAND).filter(
      (name) => name !== 'bone' && name !== 'paleSand'
    );
  }

  /** Blend a cedar tone with sand to get a warm shade. */
  blend(from, to, ratio = 0.5) {
    const parse = (hex) =>
      [1, 3, 5].map((i) => parseInt(hex.slice(i, i + 2), 16));
    const [a, b] = [parse(from), parse(to)];
    const channel = (value, i) =>
      Math.round(value * (1 - ratio) + b[i] * ratio);
    const toHex = (value) => value.toString(16).padStart(2, '0');
    return '#' + a.map(channel).map(toHex).join('');
  }

  async readGrove(file) {
    const content = await readFile(file, 'utf8');
    const lines = content.split('\n').filter(Boolean);
    return {
      grove: this.grove,
      tones: this.trees.length,
      lines: lines.length,
      content,
    };
  }
}

const grove = new CedarGrove();
const shade = grove.blend(CEDAR_SAND.forest, CEDAR_SAND.sand);

console.log(`ridge shade: ${shade}`);
