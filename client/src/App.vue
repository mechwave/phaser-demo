<template>
  <div id="pixi-canvas"></div>
</template>

<script>
import * as PIXI from "pixi.js";
import { Viewport } from "pixi-viewport";
import { mapLoader } from './loaders/mapLoader'
import MiniMap from './gui/miniMap'

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
      tilesArray: null,
      miniMap: null
    };
  },
  mounted() {
    //Create a Pixi Application
    this.app = new this.Application({
      width: 1200,
      height: 800,
      backgroundColor: 0xffffff
    });

    //Create a pixi-viewport
    this.viewport = new Viewport({
      screenWidth: 1200,
      screenHeight: 800,
      worldWidth: 1200,
      worldHeight: 800,
      interaction: this.app.renderer.plugins.interaction // the interaction module is important for wheel to work properly when renderer.view is placed or scaled
    });

    //Create Pixi particle container for background grid
    //this.container = new PIXI.ParticleContainer();

    const displayDiv = document.querySelector("#pixi-canvas");
    displayDiv.appendChild(this.app.view);
    this.app.stage.addChild(this.viewport);
    //this.viewport.addChild(this.container);

    // activate viewport plugins
    this.viewport
      .clamp({
        direction: "all"
        })
      .clampZoom({minWidth:1200, minHeight:800, maxWidth: 1200, maxHeight: 800})
      .drag()
      .pinch()
      .wheel()
      .decelerate();

    // this.setup();

    // this.viewport.on("clicked", e => {
    //   if (e.world.x > 0 && e.world.y > 0) {
    //     const x = Math.floor(e.world.x / 32) * 32;
    //     const y = Math.floor(e.world.y / 32) * 32;
    //     this.drawNewTile(x, y);
    //   }
    // });

    this.app.loader.add('maptiles', 'api/map/random', { xhrType: 'json' }).load((loader, resources) => {
        mapLoader.call(this, loader, resources)
        // console.log(this.tilesArray)
        var mm = new MiniMap(this.app);
        mm.init();
        this.app.start();
        this.app.ticker.add(function()
        { 
            //entities[1].y += 1;
            mm.update(resources.maptiles.data.tiles);
        });
    })
    this.app.stop();
  },
  methods: {
    
  }
};
</script>

<style scoped>
</style>

