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

var hexes = []

function setup() {
  createCanvas(windowWidth, windowHeight);

  for(key in dict){
    let h = new Hex(width*dict[key][0], height*dict[key][1], 0.053*height, 6);
    hexes.push(h);
  }
  console.log(hexes.length);
  
};

function mousePressed(){
  for (i in hexes){
    if (hexes[i].contains(mouseX, mouseY)){
      hexes[i].changeColor();
    }
  }
}

function draw() {
  background(100);
  stroke(10);
  
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
  
  for(i in hexes){
    hexes[i].show();
  }
}

class Hex{
  constructor(x, y, r, n) {
    this.angle = TWO_PI / n;
    this.x = x;
    this.y = y;
    this.r = r;
    this.n = n;
    this.color = color(225, 225, 225);
  }
  
  contains(mx, my){
    let d = dist(mx, my, this.x, this.y);
    if (d < this.r) {
      return true;
    } else {
      return false;
    }
  }
  
  changeColor() {
    this.color = color(0, 0, 0);
  }
  
  show() {
    beginShape();
    for (let a = 0; a < TWO_PI; a += this.angle) {
      let sx = this.x + cos(a) * this.r;
      let sy = this.y + sin(a) * this.r;
      vertex(sx, sy);
    }
    endShape(CLOSE);
    fill(this.color);
  }
}

