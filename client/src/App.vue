<template>
  <div id="pixi-canvas"></div>
</template>

<script>
import * as PIXI from "pixi.js";
import { Viewport } from "pixi-viewport";

export default {
  name: "layout",
  data() {
    return {
      app: null,
      viewport: null,
      container: null,
      Application: PIXI.Application,
      loader: PIXI.loader,
      Sprite: PIXI.Sprite,
      tiles: []
    };
  },
  mounted() {
    //Create a Pixi Application
    this.app = new this.Application({
      width: 953,
      height: 409,
      backgroundColor: 0xffffff
    });

    //Create a pixi-viewport
    this.viewport = new Viewport({
      screenWidth: 953,
      screenHeight: 409,
      worldWidth: 25000,
      worldHeight: 10000,
      interaction: this.app.renderer.plugins.interaction // the interaction module is important for wheel to work properly when renderer.view is placed or scaled
    });

    //Create Pixi particle container for background grid
    this.container = new PIXI.ParticleContainer();

    const displayDiv = document.querySelector("#pixi-canvas");
    displayDiv.appendChild(this.app.view);
    this.app.stage.addChild(this.viewport);
    this.viewport.addChild(this.container);

    // activate viewport plugins
    this.viewport
      // .clamp({direction: "all"})
      // .clampZoom({minWidth:953, minHeight:409, maxWidth: 1300, maxHeight: 1300})
      .drag()
      .pinch()
      .wheel()
      .decelerate();

    // this.setup();

    this.viewport.on("clicked", e => {
      if (e.world.x > 0 && e.world.y > 0) {
        const x = Math.floor(e.world.x / 32) * 32;
        const y = Math.floor(e.world.y / 32) * 32;
        this.drawNewTile(x, y);
      }
    });

    // this.app.loader
    //   .add("grid", require("./assets/grid.png"))
    //   .load((loader, resources) => {
    //     const grid = new PIXI.Sprite(resources.grid.texture);
    //     grid.anchor.set(0, 0);
    //     grid.scale.set(1);
    //     this.container.addChild(grid);
    //   });

    this.app.loader.add('maptiles', 'api/map/random', { xhrType: 'json' })
      .load((loader, resources) => {
        let tiles = resources.maptiles.data.tiles
        const container = new PIXI.Container();
        //app.stage.addChild(container);
        this.viewport.addChild(container)
        // Create a new texture
        const ground = PIXI.Texture.from('assets/terrains/ground.bmp');
        const sand = PIXI.Texture.from('assets/terrains/sand.bmp');

        tiles.forEach( (item) => {
            let sprite = null
            if (item.terrain == 'GROUND') {
                sprite = new PIXI.Sprite(ground);
            } else {
                sprite = new PIXI.Sprite(sand);
            }
            sprite.anchor.set(0.5);
            sprite.x = item.x*40 + 20;
            sprite.y = item.y*40 + 20;
            container.addChild(sprite);
        })
        this.app.start();
      });
    this.app.stop();
  },
  methods: {
    drawNewTile(x, y) {
      const square = new PIXI.Sprite(PIXI.Texture.WHITE);
      square.x = x;
      square.y = y;
      square.width = square.height = 25;
      square.tint = 0xc1dbe3;
      // Opt-in to interactivity
      square.interactive = true;
      square.buttonMode = true;
      this.viewport.addChild(square);
    }
  }
};
</script>

<style scoped>
</style>

