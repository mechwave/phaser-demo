import * as PIXI from 'pixi.js';
import MapsAPI from './api'
let Application			= PIXI.Application,
	Container			= PIXI.Container,
	loader				= PIXI.loader,
	resources			= PIXI.loader.resources,
	Graphics			= PIXI.Graphics,
	TextureCache		= PIXI.utils.TextureCache,
	Sprite				= PIXI.Sprite,
	Text				= PIXI.Text,
	TextStyle			= PIXI.TextStyle;


let app = new Application({
	width: 800,
	height: 800,
	antialias: true,
});

loader.add('maptiles', 'api/map/random', { xhrType: 'json' }).load(setup);

function setup() {
    let tiles = resources.maptiles.data.tiles

    const container = new PIXI.Container();
    app.stage.addChild(container);

    // Create a new texture
    const ground = PIXI.Texture.from('./assets/terrains/ground.bmp');
    const sand = PIXI.Texture.from('./assets/terrains/sand.bmp');

    tiles.forEach( (item) => {
        let sprite = null
        if (item.terrain == 'GROUND') {
            sprite = new PIXI.Sprite(ground);
        } else {
            sprite = new PIXI.Sprite(sand);
        }
        sprite.anchor.set(0.5);
        sprite.x = item.x*40 + 20
        sprite.y = item.y*40 + 20
        container.addChild(sprite);
    })
    app.start();
}

document.body.appendChild(app.view);
app.stop();