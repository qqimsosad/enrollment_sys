CREATE TABLE `course` (
  `course_id` int PRIMARY KEY,
  `title` varchar(255) NOT NULL,
  `location` varchar(255) NOT NULL,
  `start_time` varchar(255) NOT NULL,
  `end_time` varchar(255) NOT NULL,
  `syllabus` text,
  `teacher_id` int
);

CREATE TABLE `teacher` (
  `teacher_id` int PRIMARY KEY,
  `teach_account` varchar(255) UNIQUE NOT NULL,
  `teach_password` varchar(255) NOT NULL,
  `teach_name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL
);

CREATE TABLE `student` (
  `student_id` int PRIMARY KEY,
  `stu_account` varchar(255) UNIQUE NOT NULL,
  `stu_password` varchar(255) NOT NULL,
  `stu_name` varchar(255) NOT NULL
);

CREATE TABLE `enrollment` (
  `enrollment_id` int PRIMARY KEY,
  `student_id` int,
  `course_id` int,
  `enrollment_time` datetime
);

CREATE INDEX `idx_teacher_id` ON `course` (`teacher_id`);

CREATE UNIQUE INDEX `idx_teach_account` ON `teacher` (`teach_account`);

CREATE UNIQUE INDEX `idx_stu_account` ON `student` (`stu_account`);

CREATE INDEX `idx_student_id` ON `enrollment` (`student_id`);

CREATE INDEX `idx_course_id` ON `enrollment` (`course_id`);

ALTER TABLE `course` ADD FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`teacher_id`);

ALTER TABLE `enrollment` ADD FOREIGN KEY (`student_id`) REFERENCES `student` (`student_id`);

ALTER TABLE `enrollment` ADD FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`);
