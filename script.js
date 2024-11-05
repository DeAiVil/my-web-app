function showSection(sectionId) {
    document.querySelectorAll('.section').forEach((section) => {
      section.style.display = section.id === sectionId ? 'block' : 'none';
    });
  }
  