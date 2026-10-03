---
title: Contact
nav_exclude: true
permalink: /contact/
description: "Contact the team behind the European Business Wallet Requirements site: questions, corrections, contributions and partnership requests. Written to info@spherity.com."
keywords: [contact, European Business Wallet requirements, feedback]
last_verified: "2026-10-03"
---

# Contact

For questions, corrections, source suggestions or contributions, write to <a href="mailto:info@spherity.com">info@spherity.com</a>. For topics that others should see and answer, use the [GitHub discussions](https://github.com/spherity/business-wallet-requirements/discussions).

The form below prepares an email in your own mail application. It does not send data to a server, and this site stores nothing you type.

<form class="contact" id="contact-form" action="mailto:info@spherity.com" method="post" enctype="text/plain">
  <label for="c-name">Name</label>
  <input id="c-name" name="name" autocomplete="name" required>
  <label for="c-org">Organisation (optional)</label>
  <input id="c-org" name="organisation" autocomplete="organization">
  <label for="c-email">Your email address</label>
  <input id="c-email" name="email" type="email" autocomplete="email" required>
  <label for="c-topic">Topic</label>
  <select id="c-topic" name="topic">
    <option>Question about a concept or requirement</option>
    <option>Correction or source suggestion</option>
    <option>Contribution or review</option>
    <option>Ecosystem or domain input</option>
    <option>Partnership or press</option>
    <option>Other</option>
  </select>
  <label for="c-msg">Message</label>
  <textarea id="c-msg" name="message" required></textarea>
  <p><button class="btn btn-primary" type="submit">Prepare email</button></p>
</form>

<script>
(function () {
  var f = document.getElementById("contact-form");
  if (!f) return;
  f.addEventListener("submit", function (e) {
    e.preventDefault();
    var g = function (id) { return document.getElementById(id).value; };
    var body = "Name: " + g("c-name") + "\nOrganisation: " + g("c-org") + "\nEmail: " + g("c-email") + "\nTopic: " + g("c-topic") + "\n\n" + g("c-msg");
    window.location.href = "mailto:info@spherity.com?subject=" + encodeURIComponent("[EBW requirements] " + g("c-topic")) + "&body=" + encodeURIComponent(body);
  });
})();
</script>

Privacy: when you send the email, Spherity GmbH receives the data in it and uses it to answer you. Please do not send confidential information through this form.
