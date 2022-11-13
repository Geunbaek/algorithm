use std::io;

fn main(){
  let mut input = String::new();

  io::stdin().read_line(&mut input)
        .expect("Falied to read line");

  let numbers: Vec<_> = input
    .split(" ")
    .map(|num| num.trim().parse::<i32>().unwrap())
    .collect();

  println!("{}", numbers[0] + numbers[1]);
}