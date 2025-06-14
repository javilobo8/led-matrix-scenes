const fs = require('fs');

const fonts = fs.readdirSync('./src/assets/fonts').filter(file => file.endsWith('.bdf'));

const scene = [];

const fontsPerScene = 6;

for (let i = 0; i < fonts.length; i += fontsPerScene) {
  const sceneFonts = fonts.slice(i, i + fontsPerScene);
  const sceneObject = {
    duration: 2,
    elements: sceneFonts.map((font, i) => ({
      "type": "StaticText",
      "text": "23:59 " + font.replace('.bdf', ''),
      "font": font.replace('.bdf', ''),
      "color": "#ffffff",
      x: 0,
      y: i * 128 / fontsPerScene + 10,
    })),
  };
  scene.push(sceneObject);
}

fs.writeFileSync('./fonts.json', JSON.stringify(scene, null, 2), 'utf8');