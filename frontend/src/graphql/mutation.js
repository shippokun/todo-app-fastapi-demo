import gql from "graphql-tag";

export const CREATE_ACCOUNT = gql`
  mutation($email: String!, $name: String!, $password: String!) {
    CreateAccount(email: $email, name: $name, password: $password) {
      token {
        access_token
        token_type
        expires_in
      }
    }
  }
`;
