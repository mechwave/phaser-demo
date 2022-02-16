import * as PIXI from "pixi.js";
export default class Minimap {
	constructor(app) {
		this.app = app
		this.renderer = PIXI.autoDetectRenderer(200, 200);
	}
	init() {
		this.container = new PIXI.Container();
		this.background = new PIXI.Graphics();
		this.background.lineStyle(2, 0x000, 1);
		this.background.beginFill(0x050a7a, 0.25);
		this.background.drawRect(0, 0, 200, 200);
		this.background.endFill();
		this.background.cacheAsBitmap = true;
		this.container.addChild(this.background);
		this.container.x = 150;
		this.container.y = this.app.screen.height - 150;
		this.container.pivot.x = this.container.width / 2;
		this.container.pivot.y = this.container.height / 2;
		this.app.stage.addChild(this.container);
	}

	update(entities) {
		this.container.removeChildren()
		this.background.removeChildren()
		this.background.beginFill(0x650a5a, 0.25);
		this.background.drawRect(0, 0, 200, 200);
		this.background.endFill();
		for (let i = 0; i < entities.length; i += 1) {
			const px = entities[i].x // 70 * 200;
			const py = entities[i].y // 70 * 200;
			const entity = new PIXI.Graphics();
			if (entities[i].terrain == 'GROUND') {
				entity.lineStyle(1, 0xfff, 1);
				entity.beginFill(0xffffff, 0.25);
				entity.drawRect(0, 0, 1, 1);
			} else {
				entity.lineStyle(1, 0x000, 1);
				entity.beginFill(0x000000, 0.25);
				entity.drawRect(0, 0, 1, 1);
			}
			entity.endFill();
			entity.x = px;
			entity.y = py;
			this.background.addChild(entity);
		}
		let rt = PIXI.RenderTexture.create(200, 200);
		this.renderer.render(this.background, rt);
		let sprite = PIXI.Sprite.from(rt);
		//console.log(sprite)
		this.background.addChild(sprite);
		this.container.addChild(this.background);
		//this.background.removeChildren()
		//this.background.cacheAsBitmap = true;
		console.log(this.background.children.length, this.container.children.length);
		//drawing procedural texture and use it as a PIXI sprite
		// console.log(entities)
		// let sprite = new PIXI.Sprite(PIXI.Texture.Draw(function (canvas) {
		// 	//we are now in a 2D context
		// 	//you need to specify your canvas width and height otherwise it'll have a size of 0x0 and you'll get an empty sprite
		// 	canvas.width = 200;
		// 	canvas.height = 200;
		// 	var ctx = canvas.getContext('2d');  //get  canvas 2D context
		// 	ctx.fillStyle = "black";
		// 	ctx.fillRect(0,0,canvas.width,canvas.height);
		// 	var pix = ctx.createImageData(canvas.width, canvas.height);
		// 	for (let i = 0; i < entities.length.length; i ++) {
		// 		let inc = 0
		// 	//for (var y = 0; y < canvas.height; y++) {
		// 		// for (var x = 0; x < canvas.width; x++) {
		// 			//var colorRGBA = getColor(x,y);
		// 			pix.data[inc++] = 190;
		// 			pix.data[inc++] = 0;
		// 			pix.data[inc++] = 210;
		// 			pix.data[inc++] = 255;
		// 		// }
		// 	}
		// 	ctx.putImageData(pix, 0, 0);
		// }));
		// this.container.addChild(sprite);
	}
  }