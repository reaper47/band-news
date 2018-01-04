const express = require('express');
const { spawn } = require('child_process');
const webpackDevMiddleware = require('webpack-dev-middleware');
const webpack = require('webpack');
const webpackConfig = require('./webpack.config.js');
const compiler = webpack(webpackConfig);
const app = express();


/*
 * use
 *
 */
app.use(express.static(__dirname + '/www'));

app.use(webpackDevMiddleware(compiler, {
  hot: true,
  filename: 'bundle.js',
  publicPath: '/',
  stats: {
    colors: true,
  },
  historyApiFallback: true,
}));


/*
 * call python scripts
 *
 */
let runPy = new Promise((success, error) => {
  const prog = spawn('python3', ['./api/hello.py']);

  prog.stdout.on('data', data => success(data));
  prog.stdout.on('data', data => error(data));
});


/*
 * routing
 *
 */
app.get('/hi', (req, res) => {
  res.write('welcome\n');
  runPy.then(fromRunPy => {
    console.log(fromRunPy.toString());
    res.end(fromRunPy);
  });
});

const server = app.listen(3000, () => {
  const host = server.address().address;
  const port = server.address().port;
  console.log('Example app listening at http://%s:%s', host, port);
});
