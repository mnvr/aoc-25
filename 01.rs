fn main() {
    let (mut pos, mut z1, mut z2) = (50, 0, 0);
    for line in std::io::stdin().lines().map(|s| s.unwrap()) {
        let (head, tail) = line.split_at(1);
        let d = if head == "L" { -1 } else { 1 };
        let steps = tail.parse::<i32>().unwrap() * d;

        let npos = pos + steps;

        let m = npos.div_euclid(100);
        let p = npos.rem_euclid(100);

        if m < 0 && pos == 0 {
            z2 -= 1;
        }
        if m > 0 && p == 0 {
            z2 -= 1;
        }

        z1 += if p == 0 { 1 } else { 0 };
        z2 += m.abs();

        pos = p;
    }

    println!("{} {}", z1, z1 + z2);
}
