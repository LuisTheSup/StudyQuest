CREATE TABLE students (
    student_id BIGSERIAL PRIMARY KEY,
    firstname VARCHAR(100) NOT NULL,
    lastname VARCHAR (100) NOT NULL,
    email VARCHAR(255) NOT NULL DEFAULT 'Not Provided',
    phone_number VARCHAR(30) NOT NULL DEFAULT 'Not Provided',
    gender VARCHAR(10),
    date_of_birth DATE NOT NULL
);

CREATE TABLE assignments (
    assignment_id BIGSERIAL PRIMARY KEY,
    student_id BIGINT NOT NULL REFERENCES students(student_id) ON DELETE CASCADE,
    name VARCHAR(150) NOT NULL,
    description TEXT DEFAULT 'No Description',
    category VARCHAR(12) NOT NULL CHECK ( category IN ('formative', 'summative') ),
    points_achieved NUMERIC CHECK ( points_achieved >= 0 ),
    total_points NUMERIC NOT NULL CHECK ( total_points > 0 ),
    weighting REAL DEFAULT 1.0,
    grade VARCHAR(3),
    percentage VARCHAR(6),
    due_date TIMESTAMP(0) DEFAULT (NOW() + INTERVAL '1 Week')::DATE,
    graded BOOL NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP(0) DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP(0) DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT score_check CHECK ( points_achieved <= assignments.total_points )
);