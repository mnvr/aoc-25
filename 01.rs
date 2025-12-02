fn main() {
    let (mut pos, mut z1, mut z2) = (50, 0, 0);
    for line in std::io::stdin().lines().map(|s| s.unwrap()) {
        let (d, s) = line.split_at(1);
        let rot = s.parse::<i32>().unwrap();

        if d == "L" {
            pos = (100 - pos) % 100;
        }

        pos += rot;
        z2 += pos / 100;
        pos %= 100;
        z1 += if pos == 0 { 1 } else { 0 };

        if d == "L" {
            pos = (100 - pos) % 100;
        }
    }

    println!("{} {}", z1, z2);
}
