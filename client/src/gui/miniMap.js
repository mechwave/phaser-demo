import * as PIXI from "pixi.js";
export default class Minimap {
	constructor(app) {
		this.app = app
	}
	init() {
		this.container = new PIXI.Container();
		this.background = new PIXI.Graphics();
		this.background.lineStyle(2, 0x000, 1);
		this.background.beginFill(0x050a7a, 0.25);
		this.background.drawRect(0, 0, 200, 200);
		this.background.endFill();
		this.container.addChild(this.background);
		console.log(this.app.screen.width);
		this.container.x = 150;
		this.container.y = this.app.screen.height - 150;
		this.container.pivot.x = this.container.width / 2;
		this.container.pivot.y = this.container.height / 2;
		this.app.stage.addChild(this.container);
	}

	update(entities) {
		this.background.lineStyle(2, 0x000, 1);
		this.background.beginFill(0x650a5a, 0.25);
		this.background.drawRect(0, 0, 200, 200);
		this.background.endFill();
		this.container.addChild(this.background);
		for (let i = 0; i < entities.length; i += 1) {
			const px = entities[i].x / this.app.screen.width * 200;
			const py = entities[i].y / this.app.screen.height * 200;
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
			this.container.addChild(entity);
		}
		console.log(this.container.children.length);
	}
  }