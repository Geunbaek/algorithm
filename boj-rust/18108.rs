use std::io;

fn user_input() -> i32 {
  let mut input = String::new();

  io::stdin().read_line(&mut input)
    .expect("fail");
  
  return input.trim().parse::<i32>().unwrap();
}

fn main(){
  let year = user_input();

  println!("{}", year - 543);

  
}