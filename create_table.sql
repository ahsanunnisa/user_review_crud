CREATE DATABASE kulinadb;

USE kulinadb;

CREATE TABLE user_review (
    id bigint(20) AUTO_INCREMENT,
    order_id bigint(20),
    product_id bigint(20),
    user_id bigint(20),
    rating float CHECK (rating>=1 AND rating<=5),
    review text,
    created_at datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
    updated_at datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
    PRIMARY KEY (id)
);

DELIMITER ;;
CREATE trigger entityinsert BEFORE INSERT ON user_review FOR EACH ROW BEGIN SET NEW.created_at=IF(ISNULL(NEW.created_at) OR NEW.created_at='0000-00-00 00:00:00', CURRENT_TIMESTAMP, IF(NEW.created_at<CURRENT_TIMESTAMP, NEW.created_at, CURRENT_TIMESTAMP));SET NEW.updated_at=NEW.created_at; END;;
DELIMITER ;
CREATE trigger entityupdate BEFORE UPDATE ON user_review FOR EACH ROW SET NEW.updated_at=IF(NEW.updated_at<OLD.updated_at, OLD.updated_at, CURRENT_TIMESTAMP);
