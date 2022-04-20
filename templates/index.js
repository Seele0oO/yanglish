function nodejieba(sentence) {
    var nodejieba = require("nodejieba");
    var result;
    // 没有主动调用nodejieba.load载入词典的时候，
    // 会在第一次调用cut或者其他需要词典的函数时，自动载入默认词典。
    // 词典只会被加载一次。

    result = nodejieba.cut(sentence, true);
    console.log(result);
    return result;
}


