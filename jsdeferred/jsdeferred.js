

// Basic Chain
/**
next(function () {
    console.log("start");
}).
next(function () {
    function pow (x, n) {
        function _pow (n, r) {
            console.log([n, r]);
            if (n == 0) return r;
            return call(_pow, n - 1, x * r);
        }
        return call(_pow, n, 1);
    }
    return call(pow, 2, 10);
}).
next(function (r) {
    console.log([r, "end"]);
}).
error(function (e) {
    alert(e);
})
*/

// 将 next 看作 then

var Deferred = function() {
    
};

Deferred.define = function() {

};


Deferred.prototype.parallel = function() {

};


Deferred.prototype.next = function() {

};


Deferred.prototype.call = function() {

};


Deferred.prototype.loop = function() {

};


Deferred.prototype.wait = function() {

};


