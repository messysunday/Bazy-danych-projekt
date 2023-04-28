DROP TABLE IF EXISTS `bilety`;
CREATE TABLE `bilety` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cena` int(11) NOT NULL,
  `typ` varchar(45) DEFAULT NULL,
  `godzina` datetime DEFAULT NULL,
  `nazwisko` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

LOCK TABLES `bilety` WRITE;
INSERT INTO `bilety` VALUES (2,100,'delux','2020-10-10 12:12:12','kowalski'),(3,30,'normalny','2020-11-11 11:11:11','janowski'),(4,15,'ulgowy','2020-05-06 12:00:00','janusz tracz'),(5,20,'normalny','2020-02-02 12:12:12','jurczak'),(6,50,'premium','2020-05-05 10:10:10','testowy'),(7,10,'ulgowy','2020-05-05 10:10:15','testowy'),(8,20,'normalny','2020-05-05 10:10:25','testowy');
UNLOCK TABLES;

DROP TABLE IF EXISTS `dyzury`;
CREATE TABLE `dyzury` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sektor` int(11) NOT NULL,
  `pracownik` int(11) NOT NULL,
  `czynnosc` varchar(45) NOT NULL,
  `godzina_rozpoczecia` int(11) DEFAULT NULL,
  `godzina_zakonczenia` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `dyzury_fk` (`pracownik`),
  KEY `dyzury_fk2` (`sektor`),
  CONSTRAINT `dyzury_fk` FOREIGN KEY (`pracownik`) REFERENCES `pracownicy` (`id`),
  CONSTRAINT `dyzury_fk2` FOREIGN KEY (`sektor`) REFERENCES `sektory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;


LOCK TABLES `dyzury` WRITE;
INSERT INTO `dyzury` VALUES (11,1,1,'sprzatanie',8,16),(12,2,2,'sprzatanie',16,22),(13,1,3,'karmienie',8,10),(14,2,3,'karmienie',10,12),(15,3,3,'karmienie',12,14),(16,4,3,'karmienie',14,16),(17,2,7,'sprzatanie',12,14),(19,3,9,'badanie',11,15),(20,6,2,'karmienie',9,11),(21,6,7,'zamiatanie',17,20),(22,1,1,'badania',11,12),(23,3,10,'przeprowadzka',13,16),(24,4,2,'przeprowadzka',9,13),(25,6,8,'mycie szyb',10,13);
UNLOCK TABLES;

DROP TABLE IF EXISTS `pracownicy`;

CREATE TABLE `pracownicy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `imie` varchar(30) NOT NULL,
  `nazwisko` varchar(45) NOT NULL,
  `email` varchar(45) DEFAULT NULL,
  `nr_tel` int(9) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

LOCK TABLES `pracownicy` WRITE;
INSERT INTO `pracownicy` VALUES (1,'Michal','Wisniewski','ich_troje@onet.pl',181241245),(2,'Radoslaw','Majdan','twojpilkarz69@poczta.pl',664576012),(3,'Jurand','Ze Spychowa','email@email.email',510210012),(4,'Adam','Nowak','anowak@onet.pl',554779351),(5,'Dorota','Wellman','dzesika123@dzwon.eu',221684995),(6,'Agnieszka','Mikulska','xcasfjhbja@asf.cc',635415886),(7,'Jurczak','Radoslaw','pe11@nans.com',777777777),(8,'Kobylecki','Emil','emilooo@poczta.pl',684321885),(9,'Conan','Barbarzynca','nimompojecia@corobie.pl',587642211),(10,'kuba','kobyla','kk@wp.pl',123123456);
UNLOCK TABLES;


DROP TABLE IF EXISTS `sektory`;
CREATE TABLE `sektory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `specjalizacja` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;


LOCK TABLES `sektory` WRITE;
INSERT INTO `sektory` VALUES (1,'Afryka'),(2,'AmerykaPn'),(3,'AmerykaPd'),(4,'Antarktyda'),(5,'Azja'),(6,'Europa'),(7,'Australia');
UNLOCK TABLES;


DROP TABLE IF EXISTS `zagroda`;
CREATE TABLE `zagroda` (
  `id` int(11) NOT NULL,
  `sektor` int(11) NOT NULL,
  `mieszkancy` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `zagroda_fk` (`sektor`),
  CONSTRAINT `zagroda_fk` FOREIGN KEY (`sektor`) REFERENCES `sektory` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `zagroda` WRITE;
INSERT INTO `zagroda` VALUES (0,2,'alpaki'),(1,1,'slonie'),(2,1,'antylopy'),(3,1,'zyrafy'),(4,1,'jordany'),(5,1,'nosorozce'),(6,2,'orly'),(7,2,'niedzwiedzie'),(8,2,'losie'),(9,2,'rosomaki'),(10,3,'papugi'),(11,3,'kapibary'),(12,3,'krokodyle'),(13,3,'tapiry'),(14,3,'pumy'),(15,4,'pingiwiny'),(16,4,'niedzwiedzie polarne'),(17,4,'narwale'),(18,4,'foki'),(19,4,'orka'),(20,6,'wilki'),(21,5,'pandy'),(22,5,'tygrysy'),(23,5,'malpy'),(24,5,'hieny'),(25,5,'zolwie'),(26,6,'lisy'),(27,6,'mrowki'),(28,6,'skunksy'),(29,6,'rysie'),(30,7,'kangury'),(31,7,'weze'),(32,7,'koala'),(33,7,'pajaki'),(34,7,'kokabury');
UNLOCK TABLES;

DROP TABLE IF EXISTS `zwierze`;
CREATE TABLE `zwierze` (
  `sektor` int(11) NOT NULL,
  `zagroda` int(11) NOT NULL,
  `imie` varchar(45) NOT NULL,
  `gatunek` varchar(45) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `zwierze_fk2` (`sektor`),
  KEY `zwierze_fk` (`zagroda`),
  CONSTRAINT `zwierze_fk` FOREIGN KEY (`zagroda`) REFERENCES `zagroda` (`id`),
  CONSTRAINT `zwierze_fk2` FOREIGN KEY (`sektor`) REFERENCES `sektory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=80 DEFAULT CHARSET=latin1;


LOCK TABLES `zwierze` WRITE;
INSERT INTO `zwierze` VALUES (2,0,'jozia','alpaka',1),(2,0,'zuzia','alpaka',2),(1,1,'bartek','slon',3),(1,1,'kajtek','slon',4),(1,2,'ania','antylopa',5),(1,2,'asia','antylopa',6),(1,3,'jola','zyrafa',7),(1,3,'tola','zyrafa',8),(1,4,'trojki','jordany',9),(1,4,'czworki','jordany',10),(1,5,'gruby','nosorozec',11),(1,5,'chudy','nosorozec',12),(2,6,'bialy','orzel',13),(2,6,'czarny','orzel',14),(2,7,'misiu','niedzwiedz',15),(2,7,'pysiu','niedzwiedz',16),(2,8,'aztek','los',17),(2,8,'kordian','los',18),(2,9,'kicia','rosomak',19),(2,9,'kotek','rosomak',20),(3,10,'papla','papuga',21),(3,10,'klodia','papuga',22),(3,11,'marysia','kapibara',23),(3,11,'zbyszek','kapibara',24),(3,12,'michal','krokodyl',25),(3,12,'alek','krokodyl',26),(3,13,'olek','tapir',27),(3,13,'kasia','tapir',28),(3,14,'lidka','puma',29),(3,14,'makumba','puma',30),(4,15,'mugabe','pingwin',31),(4,15,'zuzanna','pingwin',32),(4,16,'bialy','niedzwiedz polarny',33),(4,16,'mlody','niedzwiedz polarny',34),(4,17,'dachowka','narwal',35),(4,17,'azbest','narwal',36),(4,18,'gruba','foka',37),(4,18,'chuda','foka',38),(4,19,'bialo czarna','orka',39),(4,19,'czarno biala','orka',40),(5,21,'slodka','panda',41),(5,21,'slona','panda',42),(5,22,'tigr','tygrys',43),(5,22,'rawr','tygrys',44),(5,23,'szymon','malpa',45),(5,23,'karpecki','malpa',46),(5,25,'bartek','zolw',47),(5,25,'tosia','zolw',48),(6,26,'jerzy','lis',49),(6,26,'wojtek','lis',50),(6,27,'sandra','mrowka',51),(6,27,'kleopatra','mrowka',52),(6,28,'smrodek','skunks',53),(6,28,'smierdziel','skunks',54),(6,29,'janusz','rys',55),(6,29,'mirek','rys',56),(7,30,'bokser','kangur',57),(7,30,'karateka','kangur',58),(7,31,'dlugi','waz',59),(7,31,'krotki','waz',60),(7,32,'brat pierwszy','koala',61),(7,32,'brat drugi','koala',62),(7,33,'jadowity','pajak',63),(7,33,'wlochaty','pajak',64),(7,34,'kalina','kokabura',65),(7,34,'karynna','kokabura',66);
UNLOCK TABLES;