object P02 extends App {

  val l = List(1,2,3,4,5,6,7,8)
  assert(penultimate(l)==7)
  assert(penultimate(List(1))=="Exception no such element")

  def penultimate[A](l:List[A])={
    if (l.length<2) "Exception no such element"
    else l(l.length-2)
  }
}
P02.main(args)