import * as Phaser from 'phaser';

const config = {
  name: 'app',
  type: Phaser.AUTO,
  width: 800,
  height: 600,
};

window.game = new Phaser.Game(config);