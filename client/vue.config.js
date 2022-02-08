const path = require("path")/* eslint-disable-line */
module.exports = {
  outputDir: path.resolve(__dirname, "../backend/src/app/templates/"),
  devServer: {
    proxy: 'http://localhost:5000'
  },
  outputDir: path.resolve(__dirname, "../server/src/app/templates/"),
}

