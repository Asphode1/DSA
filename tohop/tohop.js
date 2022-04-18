var ks = [10, 20, 20, 30, 40]
var ns = [20, 35, 40, 50, 60]
var d = new Array(100)
for (let i = 0; i < 100; i++) {
	d[i] = new Array(100)
	for (let j = 0; j < 100; j++) d[i][j] = 0
}
function dequykonho(k, n) {
	if (k == 0 || k == n) return 1
	else return dequykonho(k, n - 1) + dequykonho(k - 1, n - 1)
}

function dequyconho(k, n) {
	if (k == 0 || k == n) return 1
	if (d[k][n] != 0) return d[k][n]
	else {
		d[k][n] = dequyconho(k, n - 1) + dequyconho(k - 1, n - 1)
		return d[k][n]
	}
}

for (let i = 0; i < 5; i++) {
	var start = performance.now()
	console.log(dequyconho(ks[i], ns[i]))
	var end = performance.now()
	console.log(end - start)
}
