# Migrations

Versioned, forward-only SQL migrations. Run in order against the
target database; there's no down-migration tooling here (small
enough project that "restore from backup" is simpler than reversible
migrations) -- if that changes, introduce Alembic instead of hand-
rolled files.

```
mysql -u root -p askmql < 0001_initial_schema.sql
mysql -u root -p askmql < 0002_add_feedback_and_query_log.sql
```

New changes get a new `000N_description.sql` file -- never edit a
migration that's already been applied anywhere.
