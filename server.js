var webpack = require('webpack')
var WebpackDevServer = require('webpack-dev-server')
var config = require('./webpack.config')

new WebpackDevServer(webpack(config), {
    publicPath: config.output.publicPath,
    hot: true,
    inline: true,
    historyApiFallback: true,
    disableHostCheck: true,
    headers: {
        "Access-Control-Allow-Origin": "http://localhost:8000"
    }
}).listen(3000, function (err, result) {
    if (err) {
        console.log(err)
    }

    console.log('Listening at 0.0.0.0:3000')
})
