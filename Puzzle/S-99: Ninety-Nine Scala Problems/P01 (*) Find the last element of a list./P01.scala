object HelloWorld {  
    def main(args: Array[String]) {  
      val l = List(1,2,3,4,5,6,7,8)
      assert(last(l)==8)
    }

    def last(x:List[Int])={x(x.length-1)}
 } 
