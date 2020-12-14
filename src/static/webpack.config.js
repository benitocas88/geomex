// noinspection JSUnresolvedFunction
const path = require("path");
// noinspection JSUnresolvedFunction
const MiniCssExtractor = require("mini-css-extract-plugin");


// noinspection JSUnresolvedVariable,JSValidateTypes
module.exports = {
    entry: {
        main: "./scss/main.scss"
    },
     output: {
        filename: "js/[name].js",
        path: path.resolve(__dirname),
    },

    plugins: [
        new MiniCssExtractor({
            linkType: 'text/css',
            filename: path.join("css", "[name].css")
        })
    ],
    module: {
        rules: [{
            test: /\.(sa|sc|c)ss$/,
            use: [
                MiniCssExtractor.loader,
                "css-loader",
                "sass-loader"
            ]
        }]
    }
}
