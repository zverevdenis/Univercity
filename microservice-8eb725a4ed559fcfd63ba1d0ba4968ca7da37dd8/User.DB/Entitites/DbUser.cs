using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace User.DB.Entitites
{
    /// <summary>
    /// Модель задачи
    /// </summary>
    public class DbUser
    {
        public int Id { get; set; }

        public string FirstName { get; set; }

        public string LastName { get; set; }

        public string MiddleName { get; set; }

        public DateTimeOffset? Birthday { get; set; } = null;

        public GenderType Gender { get; set; }

        public string Email { get; set; }

        public string Phone { get; set; }

        public string Country { get; set; }

        public string City { get; set; }

        public string Password { get; set; }

        
        public DateTimeOffset CreatedAt { get; set; } = DateTimeOffset.UtcNow;

        public DateTime? DeletAt { get; set; } = null;





    }

    public enum GenderType : byte
    {
        Default = 0,

        Man = 1,

        Woman = 2
    }
}
