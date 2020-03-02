var oneTimePad = [3, 7, 2, 21, 6, 23, 12, 5, 25, 18, 18, 
    25, 24, 5, 9, 8, 20, 24, 24, 5, 9, 8, 20, 24];
var toEncrypt = "ALLYOURBASEAREBELONGTOUS".split("");
var allLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

var toReturn = [];
for (let i = 0; i < toEncrypt.length; i++) {
    toReturn.push((
        (allLetters.charCodeAt(toEncrypt[i]) + oneTimePad[i]) % 26
    ));
}
console.log(toReturn)

//var allLetters =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
