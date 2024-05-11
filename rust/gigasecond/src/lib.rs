use time::PrimitiveDateTime as DateTime;

// Returns a DateTime one billion seconds after start.
pub fn after(start: DateTime) -> DateTime {
    let mut giga_seconds = 1000000000;

    return start.checked_add(giga_seconds);
}
