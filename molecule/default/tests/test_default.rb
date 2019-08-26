# frozen_string_literal: true

describe file('/usr/local/bin/notary-client.py') do
  it { should exist }
end

describe command('/usr/local/bin/notary-client.py -h') do
  its('exit_status') { should eq 0 }
end
