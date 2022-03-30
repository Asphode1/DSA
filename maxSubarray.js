function randInt(start, end) {
	return Math.floor(Math.random() * (end - start + 1))
}

var arr = Array(10000000).fill(randInt(-1000, 1000))
var a = [4, -2, 3, -1, -5]

function bruteForce(arr) {
	var max = 0
	for (let i = 0; i < arr.length; i++) {
		for (let j = i + 1; j < arr.length; j++) {
			var sum = arr.slice(i, j).reduce((a, b) => a + b)
			max = Math.max(max, sum)
		}
	}
	return max
}

function betterBruteForce(arr) {
	var max = 0
	for (let i = 0; i < arr.length; i++) {
		var sum = 0
		for (let j = i; j < arr.length; j++) {
			sum += arr[j]
			max = Math.max(max, sum)
		}
	}
	return max
}

function dynamic(arr) {
	var s = arr[0]
	var e = arr[0]
	for (let i = 1; i < arr.length; i++) {
		e = Math.max(a[i], e + a[i])
		s = Math.max(s, e)
	}
	return s
}
/* 
var st = performance.now()
bruteForce(arr)
var ed = performance.now()
console.log(ed - st)
 */
/* st = performance.now()
betterBruteForce(arr)
ed = performance.now()
console.log(ed - st)
 */
st = performance.now()
dynamic(arr)
ed = performance.now()
console.log(ed - st)
