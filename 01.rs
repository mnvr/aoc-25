use std::io;
use std::io::BufRead;
use std::io::BufReader;

fn main() -> io::Result<()> {
    let reader = BufReader::new(io::stdin());
    let mut v: Vec<i32> = Vec::new();
    let mut pos = 50;
    let mut z = 0;

    for line in reader.lines() {
        println!("{:#?}", line);
        let s = line.unwrap();
        println!("{:#?}", s);
        let (first, rest) = s.split_at(1);
        println!("{} {}", first, rest);

        let steps: i32 = rest.parse().unwrap();
        println!("{}", steps);

        let mut isteps = steps;
        if first == "L" {
            isteps = -1 * steps;
        }
        println!("{}", isteps);
        v.push(isteps);

        let npos = pos + isteps;

        let m = npos.div_euclid(100);
        let p = npos.rem_euclid(100);

        if p == 0 {
            z += 1;
        }

        pos = p;
    }
    println!("Output: {}", z);
    // let mut input = String::new();
    // let r = io::stdin().read_line(&mut input)?;
    // println!("read_line returned:: {:#?}", r);
    // println!("You typed:: {:#?}", input.trim());
    Ok(())
}
