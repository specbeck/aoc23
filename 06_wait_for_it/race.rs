fn main() {
    let test_limit: u64 = 44707080;
    let test_record: u64 = 283113411341491;

    let mut ways: u64 = 0;

    for hold_time in 0..=test_limit {
        let boat_speed: u64 = hold_time;
        let mut clock: u64 = hold_time;
        let mut dist_covered: u64 = 0;
        while clock < test_limit {
            dist_covered += boat_speed;
            clock += 1;
        }
        if dist_covered > test_record {
            ways += 1;

        }
    }

    println!("Number of ways are {}", ways);
}