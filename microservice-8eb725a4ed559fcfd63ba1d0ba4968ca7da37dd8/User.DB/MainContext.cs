﻿using Microsoft.EntityFrameworkCore;
using User.DB.Entitites;

namespace User.DB
{
    public class MainContext : DbContext
    {
        public MainContext()
        {

        }
        public MainContext(DbContextOptions<MainContext> options)
            : base(options)
        {

        }

        public DbSet<DbUser> Users { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<DbUser>();
        }

    }   

}