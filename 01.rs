use std::error::Error;
use std::io;
use std::io::BufRead;
use std::io::BufReader;

fn main() -> Result<(), Box<dyn Error>> {
    let reader = BufReader::new(io::stdin());
    let mut pos = 50;
    let mut z = 0;

    for line in reader.lines() {
        let s = line?;
        let d = if &s[..1] == "L" { -1 } else { 1 };
        let steps = s[1..].parse::<i32>()? * d;

        let npos = pos + steps;

        let _m = npos.div_euclid(100);
        let p = npos.rem_euclid(100);

        if p == 0 {
            z += 1;
        }

        pos = p;
    }
    println!("{z}");
    Ok(())
}
