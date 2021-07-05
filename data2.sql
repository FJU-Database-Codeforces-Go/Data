-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 
-- 伺服器版本： 10.4.8-MariaDB
-- PHP 版本： 7.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `codeforces`
--

-- --------------------------------------------------------

--
-- 資料表結構 `codeforces_ratingtable`
--

CREATE TABLE `codeforces_ratingtable` (
  `type` varchar(20) NOT NULL,
  `degree` int(11) NOT NULL,
  `rating_min` int(11) NOT NULL,
  `rating_max` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `codeforces_ratingtable`
--

INSERT INTO `codeforces_ratingtable` (`type`, `degree`, `rating_min`, `rating_max`) VALUES
('user', 0, 0, 1000),
('user', 1, 1000, 1500),
('user', 2, 1500, 2000),
('user', 3, 2000, 2500),
('user', 4, 2500, 3000),
('user', 5, 3000, 4000),
('problem', 0, 0, 1000),
('problem', 1, 1000, 2000),
('problem', 2, 2000, 3000),
('problem', 3, 3000, 4000);

-- --------------------------------------------------------

--
-- 資料表結構 `codeforces_verdict`
--

CREATE TABLE `codeforces_verdict` (
  `verdict_name` varchar(20) CHARACTER SET utf8 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `codeforces_verdict`
--

INSERT INTO `codeforces_verdict` (`verdict_name`) VALUES
('TIME_LIMIT_EXCEEDED'),
('WRONG_ANSWER'),
('RUNTIME_ERROR'),
('COMPILATION_ERROR'),
('MEMORY_LIMIT_EXCEED'),
('OTHER'),
('OK');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
