import * as PIXI from "pixi.js";
let mapLoader = function(loader, resources) {
    let tiles = resources.maptiles.data.tiles
    let tileSize = resources.maptiles.data.tile_size
    let width = resources.maptiles.data.width
    let height = resources.maptiles.data.height

    //set world height and width
    this.viewport.worldWidth = width*tileSize;
    this.viewport.worldHeight = height*tileSize; 

    const container = new PIXI.Container();
    this.viewport.addChild(container)
    // Create a new texture
    const ground = PIXI.Texture.from('assets/terrains/ground.bmp');
    const sand = PIXI.Texture.from('assets/terrains/sand.bmp');
    const white = PIXI.Texture.from('assets/terrains/white.bmp');
    // this.tilesArray = Array.from(Array(width), () => new Array(height))
    tiles.forEach( (item) => {
        let sprite = null
        if (item.terrain == 'GROUND') {
            sprite = new PIXI.Sprite(ground);
        }
        else if (item.terrain == 'SAND') {
            sprite = new PIXI.Sprite(sand);
        }
        else {
            sprite = new PIXI.Sprite(white);
        }
        sprite.anchor.set(0.5);
        // tiles[item.x][item.y] = item.terrain 
        sprite.x = item.x*tileSize + tileSize/2;
        sprite.y = item.y*tileSize + tileSize/2;
        container.addChild(sprite);
    })
}
export { mapLoader }