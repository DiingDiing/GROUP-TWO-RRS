-- Create the reservations table
CREATE TABLE reservations (
    reservation_id INT AUTO_INCREMENT PRIMARY KEY,
    train VARCHAR(255),
    passenger_name VARCHAR(255),
    num_tickets INT,
    travel_class VARCHAR(255),
    fare DECIMAL(10, 2)
);

-- Create the available_seats table and insert initial data
CREATE TABLE available_seats (
    train VARCHAR(255) PRIMARY KEY,
    first_class_seats INT,
    second_class_seats INT
);

-- Insert initial data into available_seats
INSERT INTO available_seats (train, first_class_seats, second_class_seats) VALUES
    ('Train1', 50, 30),
    ('Train2', 40, 20),
    ('Train3', 60, 35);
