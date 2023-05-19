-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 19, 2023 at 07:12 PM
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
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int NOT NULL,
  `username` varchar(40) NOT NULL,
  `email` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `flag_1` text NOT NULL,
  `flag_2` text NOT NULL,
  `flag_3` text NOT NULL,
  `flag_4` text NOT NULL,
  `flag_5` text NOT NULL,
  `flag_entorno_1` tinyint(1) NOT NULL,
  `flag_entorno_2` tinyint(1) NOT NULL,
  `flag_entorno_3` tinyint(1) NOT NULL,
  `flag_entorno_4` tinyint(1) NOT NULL,
  `flag_entorno_5` tinyint(1) NOT NULL,
  `flag_usuarios_1` tinyint(1) NOT NULL,
  `flag_usuarios_2` tinyint(1) NOT NULL,
  `flag_usuarios_3` tinyint(1) NOT NULL,
  `flag_usuarios_4` tinyint(1) NOT NULL,
  `flag_usuarios_5` tinyint(1) NOT NULL,
  `flag_networking_1` tinyint(1) NOT NULL,
  `flag_networking_2` tinyint(1) NOT NULL,
  `flag_networking_3` tinyint(1) NOT NULL,
  `flag_networking_4` tinyint(1) NOT NULL,
  `flag_networking_5` tinyint(1) NOT NULL,
  `flag_archivos_1` tinyint(1) NOT NULL,
  `flag_archivos_2` tinyint(1) NOT NULL,
  `flag_archivos_3` tinyint(1) NOT NULL,
  `flag_archivos_4` tinyint(1) NOT NULL,
  `flag_archivos_5` tinyint(1) NOT NULL,
  `flag_procesos_1` tinyint(1) NOT NULL,
  `flag_procesos_2` tinyint(1) NOT NULL,
  `flag_procesos_3` tinyint(1) NOT NULL,
  `flag_procesos_4` tinyint(1) NOT NULL,
  `flag_procesos_5` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `email`, `password`, `flag_1`, `flag_2`, `flag_3`, `flag_4`, `flag_5`, `flag_entorno_1`, `flag_entorno_2`, `flag_entorno_3`, `flag_entorno_4`, `flag_entorno_5`, `flag_usuarios_1`, `flag_usuarios_2`, `flag_usuarios_3`, `flag_usuarios_4`, `flag_usuarios_5`, `flag_networking_1`, `flag_networking_2`, `flag_networking_3`, `flag_networking_4`, `flag_networking_5`, `flag_archivos_1`, `flag_archivos_2`, `flag_archivos_3`, `flag_archivos_4`, `flag_archivos_5`, `flag_procesos_1`, `flag_procesos_2`, `flag_procesos_3`, `flag_procesos_4`, `flag_procesos_5`) VALUES
(1, 'admin', 'kermitpurple96@gmail.com', 'admin123', '1', '0', '0', '0', '0', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
(2, 'paco', 'paco@paco.com', 'paco123', '1', '1', '1', '0', '0', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
(3, 'test', 'test@test.com', 'test', '0', '1', '1', '0', '0', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
(4, 'hola', 'hola@hola.com', 'hola', '1', '1', '1', '1', '1', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
(5, 'pepe', 'pepe@pepe.com', 'pepe', '1', '1', '1', '1', '0', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
(6, 'asd', 'asd@asd.com', 'asd', '1', '0', '1', '0', '0', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
(7, 'qwe', 'qwe@qwe.com', 'qwe', '1', '1', '1', '1', '0', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
(8, 'zxc', 'zxc@zxc.com', 'zxc', '1', '1', '0', '0', '0', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
(9, 'bnm', 'bnm@bnm.com', 'bnm', '0', '0', '0', '0', '0', 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
