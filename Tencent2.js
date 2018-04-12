//console.log(isValid('[]{}()'))
//num record each song's length
//dic record song's length --- song's num
//temp a kind of k contain how much other song
//supertemp store Cmn.
var calculate = function(m,n){
	if(n===0){
		return 0;
	}
	var n1=1,n2=1;
	for(var i=0;i<n;i++){
		n1=n1*m;
		m--;
	}
	for(var i=1;i<=n;i++){
		n2=n2*i
	}
	return n1/n2
} 

var fit = function(k,N,temp,result){
	if(N===0){
		console.log(k,num[N],dic[num[N]])
		if(k%num[N]===0 && k/num[N]<dic[num[N]]){
			temp.push(calculate(dic[num[N]],k/num[N]))
			var sum=1;
			for(var j=0;j<temp.length;j++){
				if(temp[j]!=0){
					sum *= temp[j]
				}
				
			}
			result[0] += sum
			console.log(result,temp)
		}
		temp.splice(0, temp.length)
	}
	else{
		for(var i=0;i<=k/num[N];i++){
			temp.push(calculate(dic[num[N]],i))
			fit(k-i*num[N],N-1,temp,result)
		}
	}
}

var dic = {2:4,3:3};
var num = [2,3];
var temp = [];
var result = [0];
fit(6,1,temp,result)
console.log(result)
console.log(calculate(5,3))




// a lena; b, lenb;
// kind : a+b
int val[] = {lena,lena,....,lenb,lenb,..b}
int k;

dp[k][kind] =dp[k][kind-1]+dp[k-val[kind]][k-1]

dp[0...k][0..kind] = 0;
dp[0][0] = 1;
for i : 1->kind;
	for v: 0->k;
		exp;