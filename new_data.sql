-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 10, 2022 at 07:42 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `new_data`
--

-- --------------------------------------------------------

--
-- Table structure for table `cars`
--

CREATE TABLE `cars` (
  `Vehical_ID` int(11) NOT NULL,
  `Model` varchar(100) NOT NULL,
  `Year` year(4) NOT NULL DEFAULT current_timestamp(),
  `is_available` tinyint(1) NOT NULL DEFAULT 1,
  `car_type` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cars`
--

INSERT INTO `cars` (`Vehical_ID`, `Model`, `Year`, `is_available`, `car_type`) VALUES
(10001, 'Camry', 2006, 1, 'Compact'),
(10002, 'Dodge', 2010, 1, 'Large'),
(10003, 'Ford', 2011, 1, 'Medium'),
(10004, 'Lexus', 2013, 1, 'SUV'),
(10005, 'Fiat', 2015, 1, 'Truck'),
(10006, 'BMW', 2020, 1, 'Van'),
(10007, 'Land Rover', 2017, 1, 'Compact'),
(10008, 'Toyota', 2021, 1, 'Large'),
(10009, 'Volvo', 2016, 1, 'Medium'),
(10010, 'Bently', 2017, 1, 'SUV'),
(10011, 'Audi', 2018, 1, 'Truck'),
(10012, 'Volks Wagen', 2020, 1, 'Van'),
(10013, 'Jeep', 2021, 1, 'Compact'),
(10014, 'Subaru', 2022, 1, 'Large'),
(10015, 'Jaguar', 2009, 1, 'Medium'),
(10016, 'Mini', 2006, 1, 'SUV'),
(10017, 'Lamborghini', 2010, 1, 'Truck'),
(10018, 'Bugattie', 2014, 1, 'Van'),
(10019, 'Ferrari', 2013, 1, 'Compact'),
(10020, 'Mercede', 2014, 1, 'Large');

-- --------------------------------------------------------

--
-- Table structure for table `car_list`
--

CREATE TABLE `car_list` (
  `car_type` varchar(100) NOT NULL,
  `daily_rates` int(11) NOT NULL,
  `weekly_rates` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `car_list`
--

INSERT INTO `car_list` (`car_type`, `daily_rates`, `weekly_rates`) VALUES
('Compact', 55, 300),
('Large', 60, 400),
('Medium', 75, 510),
('SUV', 85, 580),
('Truck', 80, 530),
('Van', 90, 600);

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `ID_no` varchar(14) NOT NULL DEFAULT uuid(),
  `FInit` char(1) NOT NULL,
  `LName` varchar(50) DEFAULT NULL,
  `Phone` char(12) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`ID_no`, `FInit`, `LName`, `Phone`) VALUES
('24', 'H', 'Kathy', '650-969-7296'),
('f3faa42b-ce54-', 'A', 'Tammy', '650-323-8567'),
('f3fab55f-ce54-', 'B', 'Bill', '650-236-3345'),
('f3fb0346-ce54-', 'B', 'Sue', '650-221-3459'),
('f3fb0b15-ce54-', 'B', 'Barbara', '650-922-1235'),
('f3fb0efa-ce54-', 'C', 'John', '652-788-2979'),
('f3fb157a-ce54-', 'C', 'Scott', '650-335-9032'),
('f3fb1b10-ce54-', 'C', 'Don', '650-223-4502'),
('f3fb1fbd-ce54-', 'D', 'Martin', '650-223-4598'),
('f3fb2459-ce54-', 'D', 'Jan', '650-977-3883'),
('f3fb26d3-ce54-', 'E', 'Kelly', '655-875-0058'),
('f3fb291a-ce54-', 'E', 'John', '650-198-2433'),
('f3fb2b6c-ce54-', 'G', 'Ruth ', '650-323-8911'),
('f3fb3002-ce54-', 'H', 'Marco', '650-723-8901'),
('f3fb33df-ce54-', 'K', 'Sandra', '650-256-8119'),
('f3fb3658-ce54-', 'H', 'Kathy', '650-969-7296');

-- --------------------------------------------------------

--
-- Table structure for table `rentals`
--

CREATE TABLE `rentals` (
  `Start_Date` date NOT NULL DEFAULT current_timestamp(),
  `Rental_ID` varchar(100) NOT NULL DEFAULT '0',
  `weekly_rental` tinyint(1) NOT NULL DEFAULT 0,
  `daily_rental` tinyint(1) NOT NULL DEFAULT 0,
  `num_days` int(11) NOT NULL DEFAULT 0,
  `num_weeks` int(11) NOT NULL DEFAULT 0,
  `Return_Date` date NOT NULL DEFAULT (`Start_Date` + interval `num_days` + `num_weeks` * 7 day)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rentals`
--

INSERT INTO `rentals` (`Start_Date`, `Rental_ID`, `weekly_rental`, `daily_rental`, `num_days`, `num_weeks`, `Return_Date`) VALUES
('2023-08-01', '238973961', 0, 1, 10, 0, '2023-08-11'),
('2022-08-01', '461576375', 1, 0, 0, 10, '2022-10-10'),
('2023-01-01', '470263848', 0, 1, 3, 0, '2023-01-04'),
('2022-06-22', 'A1225', 1, 0, 0, 1, '2022-06-29'),
('2022-07-06', 'A1236', 0, 1, 5, 0, '2022-07-11'),
('2022-09-01', 'A1247', 1, 0, 0, 3, '2022-09-22'),
('2022-08-01', 'A1322', 0, 1, 10, 0, '2022-08-11'),
('2022-10-23', 'A1333', 1, 0, 0, 2, '2022-11-06'),
('2022-05-07', 'A1340', 0, 1, 3, 0, '2022-05-10'),
('2022-08-14', 'A1344', 0, 1, 1, 0, '2022-08-15'),
('2022-06-01', 'A1373', 1, 0, 0, 2, '2022-06-15'),
('2022-07-12', 'A1458', 0, 1, 1, 0, '2022-07-13'),
('2022-10-01', 'A1469', 1, 0, 0, 1, '2022-10-08'),
('2022-07-14', 'A1470', 0, 1, 9, 0, '2022-07-23'),
('2022-10-09', 'A1481', 1, 0, 0, 1, '2022-10-16'),
('2022-05-20', 'A1562', 0, 1, 4, 0, '2022-05-24'),
('2022-05-11', 'A1651', 1, 0, 0, 1, '2022-05-18'),
('2022-06-17', 'A1994', 0, 1, 1, 0, '2022-06-18');

-- --------------------------------------------------------

--
-- Table structure for table `rents`
--

CREATE TABLE `rents` (
  `Rental_Id` varchar(100) NOT NULL,
  `ID_no` varchar(14) NOT NULL DEFAULT uuid(),
  `Vehical_Id` int(11) NOT NULL,
  `is_active` tinyint(1) NOT NULL DEFAULT 0,
  `is_scheduled` tinyint(1) NOT NULL DEFAULT 0,
  `Amount_due` varchar(100) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rents`
--

INSERT INTO `rents` (`Rental_Id`, `ID_no`, `Vehical_Id`, `is_active`, `is_scheduled`, `Amount_due`) VALUES
('A1340', 'f3faa42b-ce54-', 10001, 0, 0, '$20.00'),
('A1651', 'f3fab55f-ce54-', 10002, 0, 0, '$30.00'),
('A1562', 'f3fb0346-ce54-', 10003, 0, 0, '$40.00'),
('A1373', 'f3fb0b15-ce54-', 10004, 0, 0, '$50.00'),
('A1994', 'f3fb0efa-ce54-', 10005, 0, 0, '$60.00'),
('A1225', 'f3fb157a-ce54-', 10006, 0, 0, '$70.00'),
('A1236', 'f3fb1b10-ce54-', 10007, 0, 0, '$80.00'),
('A1247', 'f3fb1fbd-ce54-', 10008, 0, 0, '$90.00'),
('A1458', 'f3fb2459-ce54-', 10009, 0, 0, '$100.00'),
('A1469', 'f3fb26d3-ce54-', 10010, 0, 0, '$110.00'),
('A1470', 'f3fb291a-ce54-', 10011, 0, 0, '$120.00'),
('A1481', 'f3fb2b6c-ce54-', 10012, 0, 0, '$130.00'),
('A1322', 'f3fb3002-ce54-', 10013, 0, 0, '$140.00'),
('A1333', 'f3fb33df-ce54-', 10014, 0, 0, '$150.00'),
('A1344', 'f3fb3658-ce54-', 10015, 0, 0, '$160.00'),
('238973961', 'f3fb3658-ce54-', 10016, 0, 0, '$200.00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cars`
--
ALTER TABLE `cars`
  ADD PRIMARY KEY (`Vehical_ID`),
  ADD KEY `car_type` (`car_type`);

--
-- Indexes for table `car_list`
--
ALTER TABLE `car_list`
  ADD PRIMARY KEY (`car_type`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`ID_no`);

--
-- Indexes for table `rentals`
--
ALTER TABLE `rentals`
  ADD PRIMARY KEY (`Rental_ID`);

--
-- Indexes for table `rents`
--
ALTER TABLE `rents`
  ADD PRIMARY KEY (`ID_no`,`Vehical_Id`,`Rental_Id`),
  ADD KEY `rentsC1` (`Vehical_Id`),
  ADD KEY `rentsC3` (`Rental_Id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `cars`
--
ALTER TABLE `cars`
  ADD CONSTRAINT `cars_ibfk_1` FOREIGN KEY (`car_type`) REFERENCES `car_list` (`car_type`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `rents`
--
ALTER TABLE `rents`
  ADD CONSTRAINT `rentsC1` FOREIGN KEY (`Vehical_Id`) REFERENCES `cars` (`Vehical_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `rentsC2` FOREIGN KEY (`ID_no`) REFERENCES `customers` (`ID_no`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `rentsC3` FOREIGN KEY (`Rental_Id`) REFERENCES `rentals` (`Rental_ID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
