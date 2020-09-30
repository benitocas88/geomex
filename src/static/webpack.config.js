// noinspection JSUnresolvedFunction
const path = require("path");
// noinspection JSUnresolvedFunction
const MiniCssExtractor = require("mini-css-extract-plugin");


// noinspection JSUnresolvedVariable
module.exports = {
    entry: {
        main: "./scss/main.scss"
    },
    output: {
        filename: "js/[name].js",
        path: path.resolve(__dirname),
    },
    plugins: [
        new MiniCssExtractor({ filename: "css/[name].css" })
    ],
    module: {
        rules: [
            {
                test: /\.(sa|sc|c)ss$/,
                loader: [
                    MiniCssExtractor.loader,
                    "css-loader",
                    "sass-loader"
                ]
            }
        ]
    }
}
