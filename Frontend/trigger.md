```sql
create table test2 (
	id serial not null primary key,
	tid INTEGER not null,
	state text not null
);

create table test1 (
	id serial not null primary key,
	tid INTEGER not null,
	state text not null
);

DROP TABLE test1;

insert into test1 (tid, state) values (1, 'active') returning *;
insert into test2 (tid, state) values (1, 'active') returning *;
update test1 set state = 'finished' where tid = 1 returning *;
update test1 set state = 'failed' where tid = 1 returning *;
select * from test2;

CREATE OR REPLACE FUNCTION test1() RETURNS TRIGGER AS $$
BEGIN
	UPDATE test2
	SET state = NEW.state
	WHERE tid = NEW.tid;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER test1
AFTER UPDATE ON test1
FOR EACH ROW
WHEN (OLD.state IS DISTINCT FROM NEW.state)
EXECUTE PROCEDURE test1();
```
