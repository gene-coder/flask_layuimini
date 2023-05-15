// 生成uuid
function generateUUID(length) {
    var chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'.split('');
    var uuid = [], rnd = Math.random, r;
    for (var i = 0; i < length; i++) {
        r = 0 | rnd() * 62;
        uuid[i] = chars[r];
    }
    return uuid.join('');
  }
  