use std::error::Error;
use std::io;
use std::io::BufRead;
use std::io::BufReader;

fn main() -> Result<(), Box<dyn Error>> {
    let reader = BufReader::new(io::stdin());
    let mut pos = 50;
    let mut z1 = 0;
    let mut z2 = 0;

    for line in reader.lines() {
        let s = line?;
        let d = if &s[..1] == "L" { -1 } else { 1 };
        let steps = s[1..].parse::<i32>()? * d;

        let npos = pos + steps;

        let mut m = npos.div_euclid(100);
        let p = npos.rem_euclid(100);

        if m < 0 && pos == 0 {
            m += 1;
        }
        if m > 0 && p == 0 {
            m -= 1;
        }

        z1 += if p == 0 { 1 } else { 0 };
        z2 += m.abs();

        pos = p;
    }
    println!("{} {}", z1, z1 + z2);
    Ok(())
}
