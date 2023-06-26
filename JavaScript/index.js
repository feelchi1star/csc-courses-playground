class Data {
  constructor(name, cid) {
    this.name = name;
    this.cid = cid;
  }

  Logging() {
    console.log(this.name, this.cid);
  }
}
const data1 = new Data("Felix", "32232");
console.log(data1);
