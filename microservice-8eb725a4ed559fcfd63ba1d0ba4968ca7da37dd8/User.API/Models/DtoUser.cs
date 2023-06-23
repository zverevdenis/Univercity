using System.ComponentModel.DataAnnotations;
using User.DB.Entitites;

namespace User.API.Models
{
    public class DtoUser
    {
        public int Id { get; set; }

        [Required]
        public string FirstName { get; set; }

        [Required]
        public string LastName { get; set; }

        public string? MiddleName { get; set; }

        public DateTimeOffset? Birthday { get; set; } = null;

        public GenderType Gender { get; set; }

        public string Email { get; set; }

        public string Phone { get; set; }
        

        public string Country { get; set; }

        public string City { get; set; }

        public string Password { get; set; }

        

       
    }
}
