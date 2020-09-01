function setup() {
  createCanvas(900, 500);
};

function draw() {
  background(100);
  stroke(10);
  
   var dict = {0:[0.2,0.25],
  1:[0.3,0.25],2:[0.4,0.25],
  3:[0.5,0.25],4:[0.6,0.25],5:[0.7,0.25],
  6:[0.15,0.4],
  7:[0.25,0.4],8:[0.35,0.4],9:[0.45,0.4],10:[0.55,0.4],
  11:[0.65,0.4],12:[0.75,0.4],
  13:[0.2,0.55],14:[0.3,0.55],
  15:[0.4,0.55],16:[0.5,0.55],
  17:[0.6,0.55],18:[0.7,0.55],
  19:[0.8,0.55],20:[0.5,0.7]
  };

  var arestas = {0:[0,1],1:[1,2],2:[2,3],3:[3,4],4:[4,5],
  5:[1,7],6:[2,9],7:[3,9],8:[3,10],9:[5,11],10:[6,7],
  11:[7,8],12:[8,9],13:[9,10],14:[10,11],15:[11,18],16:[12,18],
  17:[6,13],18:[7,14],19:[8,15],20:[9,16],21:[10,16],
  23:[15,16],24:[16,17],25:[17,18],26:[18,19],27:[15,20],
  29:[16,20],30:[17,20]
  };
  
  for(var e in arestas){
    var a = arestas[e][0];
    var b = arestas[e][1];
    var x1 = dict[a][0];
    var x2 = dict[b][0];
    var y1 = dict[a][1];
    var y2 = dict[b][1];
    
    line(width*x1, height*y1, width*x2, height*y2);
  }

  //line(width0.2, height0.1, width0.3, height0.1);
  for(var key in dict){
    polygon(width*dict[key][0], height*dict[key][1], 0.053*height, 6);
  }
}

function polygon(x, y, radius, npoints) {
  this.clicked = function(){
    this.col = color(255,0,200);
  }
  let angle = TWO_PI / npoints;
  beginShape();
  for (let a = 0; a < TWO_PI; a += angle) {
    let sx = x + cos(a) * radius;
    let sy = y + sin(a) * radius;
    vertex(sx, sy);
  }
  endShape(CLOSE);
}