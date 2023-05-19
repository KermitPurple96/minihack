-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 19, 2023 at 07:10 PM
-- Server version: 8.0.33-0ubuntu0.22.04.2
-- PHP Version: 8.1.2-1ubuntu2.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `minihack`
--

-- --------------------------------------------------------

--
-- Table structure for table `flags`
--

CREATE TABLE `flags` (
  `flag_id` int NOT NULL,
  `flag_comandos` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `flag_entorno` varchar(50) NOT NULL,
  `flag_usuarios` varchar(50) NOT NULL,
  `flag_networking` varchar(50) NOT NULL,
  `flag_archivos` varchar(50) NOT NULL,
  `flag_procesos` varchar(50) NOT NULL,
  `sol_comandos` varchar(50) NOT NULL,
  `sol_entorno` varchar(50) NOT NULL,
  `sol_usuarios` varchar(50) NOT NULL,
  `sol_networking` varchar(50) NOT NULL,
  `sol_archivos` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `flags`
--

INSERT INTO `flags` (`flag_id`, `flag_comandos`, `flag_entorno`, `flag_usuarios`, `flag_networking`, `flag_archivos`, `flag_procesos`, `sol_comandos`, `sol_entorno`, `sol_usuarios`, `sol_networking`, `sol_archivos`) VALUES
(1, 'DurRwQHbjUTmfG3Wk6p7PeC9B', 'xc2IGhTCu4BLNQa0nZes3VFyl', 'KNR1ElmgX7IcHqfD96QuZvnUr', 'jIbouKk4G2BAyLixFQJM0mEYH', '9N3TKbA8rXnIpe40Dz5Q1oLRa', 'tjnKy82fHxO4TUJFcPLo6wmvd', 'KdLbAoYqGTc5ZQpIz87gH3VJt', 'gDqOpl5RI4rLHcUk97NFwP0av', 'LM7C8kBESJxVe3pAbzvI4rDF5', 'Dil1HAI0Qfmwt8NjChvzVX5ET', 't0KSLJE4WGzl8BPmkMxHbsd25'),
(2, 'cpgNUndrSsqQ7IGP2B4TlM0LR', 'l06Q8AmkDiLST3hfGVjNOUECM', 'dG5IuCMbOsf2qe6TEoyFmAaYZ', 'Iuo14iAWg95mTESG3y0LsJf8a', 'MoYxsX1mcKNA4zwftinkGa3Wb', 'rFHDxsMCwRES1i5I84JjdLO9b', 't4V9HLGxeNfWl5hYmErpMbaB2', 'hd6QWmX7AtHxf3GK5IJ0CN4Mo', 'xGi50EWz29DkuYsBepq1PbTrV', 'xV3vASW2u1MeOq0yXgPdfLN5t', 'jpZ7GYn2NIKUxtTzfF9CcAPE1'),
(3, 'Gf4I6Olgs3RkFrx25yS7AtYQb', '19cpd5mQ6mfPz5nAal28v6pxq', 'EJYUCc7bkxj641dzaVKrlf9t5', '15tRvbhU4G9uFBYZ3JCVrf7zP', 'sYhLHf4NRDdyjnwm6BAMxeb3o', 'D8XkFEGjemWyrwLQqi9ndBHOb', 'FdiZt2mf8O4vKeljNrh6qAJTs', '9H6iOx3ILdcFp2S4mVuyAhUkE', 'sF0QTLnBiwoU3u4zfZVjGlgCb', 'OqFu0B4iGgUC3tYrhnQ8Sbk9V', 'XKvxN52T48GQ6atJzU1rLwRbu'),
(4, '1VFkaL2ZuEHhwJOjdrYX7U0B9', 'G7Kv31dmwTXAPfrNZVSoh6Ikl', 'lGTemUOb6Y0q7FQBAg8CLVndP', 'C28PmNQqbE5WUIah0FvHT9tA3', 'koRQYPlXcFC0JMbuv1VUmsOq2', 'WFtaGpKQvHj928NoSrxikhzRJ', 'disAnJIyTchgmvz20pFr1oVSD', '7HEiYgDsyknrldZzA6RSFav5B', 'zaiRdq90ylPOI57XCFb6kemxu', 'RxpTuBPE6nMf1KG0S8bvQmYUD', '59zubHRT8QtZEI4JAhfBUpd2j'),
(5, 'eTxWFAL1QDNfG5w4cHZJr7IEi', 'NOaJ4nrIe2lcdpAFbfvG5B8Ku', 'cFfhWKVz2961qRCJldyBNiaIu', '7hL1BjtA3lm2uTiEKwpO5JUHN', 'vTcMVyiLhsu6BXOP1YEpFbd4A', 'Ae0PXTk3s4F7mypSQjxMRHvzd', 'QRnrBHpiItqay9k6F3AjChuDV', 'khDQP6T4mNLfHKCYnRUw1IFVJ', 'BjELkTcGNwDi0anIlhCxV5s3Y', 'l3IPpVxW1tHUCRr9heBMEzOLq', '7dm4TXPZe3I9icuhEM5kaL1nV'),
(6, 'DurRwQHbjUTmfG3Wk6p7PeC9B', 'xc2IGhTCu4BLNQa0nZes3VFyl', 'KNR1ElmgX7IcHqfD96QuZvnUr', 'jIbouKk4G2BAyLixFQJM0mEYH', '9N3TKbA8rXnIpe40Dz5Q1oLRa', 'tjnKy82fHxO4TUJFcPLo6wmvd', 'KdLbAoYqGTc5ZQpIz87gH3VJt', 'gDqOpl5RI4rLHcUk97NFwP0av', 'LM7C8kBESJxVe3pAbzvI4rDF5', 'Dil1HAI0Qfmwt8NjChvzVX5ET', 't0KSLJE4WGzl8BPmkMxHbsd25'),
(7, 'cpgNUndrSsqQ7IGP2B4TlM0LR', 'l06Q8AmkDiLST3hfGVjNOUECM', 'dG5IuCMbOsf2qe6TEoyFmAaYZ', 'Iuo14iAWg95mTESG3y0LsJf8a', 'MoYxsX1mcKNA4zwftinkGa3Wb', 'rFHDxsMCwRES1i5I84JjdLO9b', 't4V9HLGxeNfWl5hYmErpMbaB2', 'hd6QWmX7AtHxf3GK5IJ0CN4Mo', 'xGi50EWz29DkuYsBepq1PbTrV', 'xV3vASW2u1MeOq0yXgPdfLN5t', 'jpZ7GYn2NIKUxtTzfF9CcAPE1'),
(8, 'Gf4I6Olgs3RkFrx25yS7AtYQb', '19cpd5mQ6mfPz5nAal28v6pxq', 'EJYUCc7bkxj641dzaVKrlf9t5', '15tRvbhU4G9uFBYZ3JCVrf7zP', 'sYhLHf4NRDdyjnwm6BAMxeb3o', 'D8XkFEGjemWyrwLQqi9ndBHOb', 'FdiZt2mf8O4vKeljNrh6qAJTs', '9H6iOx3ILdcFp2S4mVuyAhUkE', 'sF0QTLnBiwoU3u4zfZVjGlgCb', 'OqFu0B4iGgUC3tYrhnQ8Sbk9V', 'XKvxN52T48GQ6atJzU1rLwRbu'),
(9, '1VFkaL2ZuEHhwJOjdrYX7U0B9', 'G7Kv31dmwTXAPfrNZVSoh6Ikl', 'lGTemUOb6Y0q7FQBAg8CLVndP', 'C28PmNQqbE5WUIah0FvHT9tA3', 'koRQYPlXcFC0JMbuv1VUmsOq2', 'WFtaGpKQvHj928NoSrxikhzRJ', 'disAnJIyTchgmvz20pFr1oVSD', '7HEiYgDsyknrldZzA6RSFav5B', 'zaiRdq90ylPOI57XCFb6kemxu', 'RxpTuBPE6nMf1KG0S8bvQmYUD', '59zubHRT8QtZEI4JAhfBUpd2j'),
(10, 'eTxWFAL1QDNfG5w4cHZJr7IEi', 'NOaJ4nrIe2lcdpAFbfvG5B8Ku', 'cFfhWKVz2961qRCJldyBNiaIu', '7hL1BjtA3lm2uTiEKwpO5JUHN', 'vTcMVyiLhsu6BXOP1YEpFbd4A', 'Ae0PXTk3s4F7mypSQjxMRHvzd', 'QRnrBHpiItqay9k6F3AjChuDV', 'khDQP6T4mNLfHKCYnRUw1IFVJ', 'BjELkTcGNwDi0anIlhCxV5s3Y', 'l3IPpVxW1tHUCRr9heBMEzOLq', '7dm4TXPZe3I9icuhEM5kaL1nV');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `flags`
--
ALTER TABLE `flags`
  ADD PRIMARY KEY (`flag_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `flags`
--
ALTER TABLE `flags`
  MODIFY `flag_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
